import React, { useState } from 'react';
import Header from './components/header.js';
import Heartbeat from './components/Heartbeat.js';
import Sleep from './components/Sleep.js';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
} from 'chart.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import healthData from "./test_file.json";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const astronaut_dict = {
  0: "astronaut1",
  1: "astronaut2",
  2: "astronaut3",
  3: "astronaut4"
};

const astronaut_dict_color = {
  0: "rgba(75,192,192,",
  1: "rgba(192,75,192,",
  2: "rgba(192,192,75,",
  3: "rgba(75,75,192,"
};

function processHeartbeatData(healthData) {
  let astronaut_Heartbeat_Data = [[], [], [], []];
  let astronaut_Heartbeats_Chartdata = [];
  let numHeartbeats = 0;

  for (let day = 0; day < healthData.length; day++) {
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      numHeartbeats = healthData[day][astronaut_dict[astronautNum]].heartrate_bpm.length;
      for (let heartbeat = 0; heartbeat < numHeartbeats; heartbeat++) {
        astronaut_Heartbeat_Data[astronautNum].push(healthData[day][astronaut_dict[astronautNum]].heartrate_bpm[heartbeat]);
      }
    }
  }

  for (let i = 0; i < 4; i++) {
    const modifiedLabels = astronaut_Heartbeat_Data[i].map((_, index) => {
      return (index % 360 === 0) ? `day ${index / 360}` : '';
    });

    astronaut_Heartbeats_Chartdata[i] = {
      labels: modifiedLabels,
      datasets: [{
        label: 'Astronaut ' + (i + 1) + '\'s Heartbeats',
        data: astronaut_Heartbeat_Data[i],
        borderWidth: 1,
        borderColor: astronaut_dict_color[i] + '1)',
        backgroundColor: astronaut_dict_color[i] + '0.2)',
      }]
    };
  }

  return astronaut_Heartbeats_Chartdata;
}

function processSleepData(healthData) {
  let astronaut_Sleep_Data = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []]
  ];
  let astronaut_Sleep_Chartdata = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []]
  ];

  for (let day = 0; day < healthData.length; day++) {
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      astronaut_Sleep_Data[astronautNum][0].push(healthData[day][astronaut_dict[astronautNum]].previous_night_awake_minutes);
      astronaut_Sleep_Data[astronautNum][1].push(healthData[day][astronaut_dict[astronautNum]].previous_night_light_minutes);
      astronaut_Sleep_Data[astronautNum][2].push(healthData[day][astronaut_dict[astronautNum]].previous_night_deep_minutes);
      astronaut_Sleep_Data[astronautNum][3].push(healthData[day][astronaut_dict[astronautNum]].previous_night_rem_minutes);
    }
  }

  for (let i = 0; i < 4; i++) {
    const dayLabels = astronaut_Sleep_Data[i][0].map((_, index) => {
      return `day ${index + 1}`;
    });

    for (let j = 0; j < 4; j++) {
      astronaut_Sleep_Chartdata[i][j] = {
        labels: dayLabels,
        datasets: [{
          label: 'Astronaut ' + (i + 1) + '\'s Sleep',
          data: astronaut_Sleep_Data[i][j],
          borderWidth: 1,
          borderColor: astronaut_dict_color[i] + '1)',
          backgroundColor: astronaut_dict_color[i] + '0.2)',
        }]
      };
    }
  }

  return astronaut_Sleep_Chartdata;
}

function processFoodData(healthData) {
  let astronaut_Food_Data = [];

  let meal1 = 0;
  let meal2 = 0;
  let meal3 = 0;
  for (let day = 0; day < healthData.length; day++) {
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      if (!astronaut_Food_Data[astronautNum]) {
        astronaut_Food_Data[astronautNum] = [];
      }
      if (!astronaut_Food_Data[astronautNum][day]) {
        astronaut_Food_Data[astronautNum][day] = [[], [], []];
      }
      let temp = healthData[day][astronaut_dict[astronautNum]];
      meal1 = parseFloat(temp.meal_1_breakfast) + parseFloat(temp.meal_2_breakfast) * 2 + parseFloat(temp.meal_3_breakfast) * 3;
      meal2 = parseFloat(temp.meal_1_lunch) + parseFloat(temp.meal_2_lunch) * 2 + parseFloat(temp.meal_3_lunch) * 3;
      meal3 = parseFloat(temp.meal_1_dinner) + parseFloat(temp.meal_2_dinner) * 2 + parseFloat(temp.meal_3_dinner) * 3;
      console.log("Day: ", day);
      console.log(meal1, meal2, meal3);

      astronaut_Food_Data[astronautNum][day][0].push(meal1);
      astronaut_Food_Data[astronautNum][day][1].push(meal2);
      astronaut_Food_Data[astronautNum][day][2].push(meal3);
    }
  }

  return astronaut_Food_Data;
}

export default function App() {

  // let the max number of days be 7, and cut off the start of the data if it is longer than 7 days
  let max = 8;
  if (healthData.length > max) {
    healthData = healthData.slice(healthData.length - max, healthData.length);
  }

  const [formParams, setFormParams] = useState({
    astronaut: '',
  });

  const handleButtonClick = (astronaut) => {
    setFormParams({ astronaut });
  }

  // Temp data to fill graphs with to test how visuals look
  const labels = ['5', '4', '3', '2', '1', '0'];
  const tempdata = {
    labels,
    datasets: [{
      label: '# of Votes',
      data: [120, 190, 70, 50, 80, 90],
      borderWidth: 1,
      borderColor: 'rgba(75,192,192,1)',
      backgroundColor: 'rgba(75,192,192,0.2)',
    }]
  };

  // Start the heartbeat data transfer from the json file

  const astronaut_Heartbeats_Chartdata = processHeartbeatData(healthData);

  // Start the sleep data transfer from the json file

  const astronaut_Sleep_Chartdata = processSleepData(healthData);

  // Start the food data transfer from the json file
  // Since this is just in a table, we don't need to make a chart for it
  const astronaut_Food_Data = processFoodData(healthData);

  return (
    <div>
      <Header />
      <div className="container-fluid">
        <div className="row" style={{ minHeight: '200px' }}>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[0]} text={"Heartbeat of Astronaut 1"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[1]} text={"Heartbeat of Astronaut 2"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[2]} text={"Heartbeat of Astronaut 3"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[3]} text={"Heartbeat of Astronaut 4"} />
          </div>
          <div className="col-md-3">
            <h3>Astronaut 1 Food Data</h3>
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th>Day</th>
                  <th>Breakfast</th>
                  <th>Lunch</th>
                  <th>Dinner</th>
                </tr>
              </thead>
              <tbody>
                {astronaut_Food_Data[0].map((dayData, dayIndex) => (
                  <tr key={dayIndex}>
                    <td>{`Day ${dayIndex + 1}`}</td>
                    <td>{dayData[0]}</td>
                    <td>{dayData[1]}</td>
                    <td>{dayData[2]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="col-md-3">
            <h3>Astronaut 2 Food Data</h3>
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th>Day</th>
                  <th>Breakfast</th>
                  <th>Lunch</th>
                  <th>Dinner</th>
                </tr>
              </thead>
              <tbody>
                {astronaut_Food_Data[1].map((dayData, dayIndex) => (
                  <tr key={dayIndex}>
                    <td>{`Day ${dayIndex + 1}`}</td>
                    <td>{dayData[0]}</td>
                    <td>{dayData[1]}</td>
                    <td>{dayData[2]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="col-md-3">
            <h3>Astronaut 3 Food Data</h3>
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th>Day</th>
                  <th>Breakfast</th>
                  <th>Lunch</th>
                  <th>Dinner</th>
                </tr>
              </thead>
              <tbody>
                {astronaut_Food_Data[2].map((dayData, dayIndex) => (
                  <tr key={dayIndex}>
                    <td>{`Day ${dayIndex + 1}`}</td>
                    <td>{dayData[0]}</td>
                    <td>{dayData[1]}</td>
                    <td>{dayData[2]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="col-md-3">
            <h3>Astronaut 4 Food Data</h3>
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th>Day</th>
                  <th>Breakfast</th>
                  <th>Lunch</th>
                  <th>Dinner</th>
                </tr>
              </thead>
              <tbody>
                {astronaut_Food_Data[3].map((dayData, dayIndex) => (
                  <tr key={dayIndex}>
                    <td>{`Day ${dayIndex + 1}`}</td>
                    <td>{dayData[0]}</td>
                    <td>{dayData[1]}</td>
                    <td>{dayData[2]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        
      </div>
      <hr style={{ border: '2px solid black', margin: '20px 0' }} />
      <div className="button-container" style={{ textAlign: 'center', margin: '20px 0' }}>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(1)}>1</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(2)}>2</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(3)}>3</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(4)}>4</button>
      </div>
      <div className="text-box" style={{ textAlign: 'center', margin: '20px 0' }}>
        <input type="text" value={"Astronaut " + formParams.astronaut + ":"} readOnly className="form-control text-center" />
      </div>
      <div className="container-fluid" style={{ padding: "5px" }}>
        {formParams.astronaut && astronaut_Sleep_Chartdata[parseInt(formParams.astronaut) - 1] && (
          <div className="row justify-content-center" style={{ minHeight: '200px' }}>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][1]} text={"Amount of light sleep"} />
            </div>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][2]} text={"Amount of heavy sleep"} />
            </div>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][3]} text={"Amount of REM sleep"} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
