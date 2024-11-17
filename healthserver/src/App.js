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

const labels = ['5', '4', '3', '2', '1', '0'];

export default function App() {
  const [formParams, setFormParams] = useState({
    astronaut: '',
  });

  const handleButtonClick = (astronaut) => {
    setFormParams({ astronaut });
  }

  // Temp data to fill graphs with to test how visuals look
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

  let astronaut_dict = {
    0: "astronaut1",
    1: "astronaut2",
    2: "astronaut3",
    3: "astronaut4"
  };

  // Start the heartbeat data transfer from the json file

  let astronaut_Heartbeat_Data = [[],[],[],[]];
  let numHeartbeats = 0
  let astronaut_Heartbeats_Chartdata = [];

  //console.log("healthdata lengh: " + healthData.length);
  //console.log(healthData[0][astronaut_dict[0]].heartrate_bpm);
  for (let day = 0; day < healthData.length; day++) {
    //console.log("There are " + healthData[day].length + " astronauts on day " + day);
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      numHeartbeats = healthData[day][astronaut_dict[astronautNum]].heartrate_bpm.length;
      // log the amount of heartbeats for each astronaut
      //console.log("Astronaut " + astronautNum + " has " + numHeartbeats + " heartbeats on day " + day);
      
      // append each atronaut's heartbeat data to the array
      for (let heartbeat = 0; heartbeat < numHeartbeats; heartbeat++) {
        astronaut_Heartbeat_Data[astronautNum].push(healthData[day][astronaut_dict[astronautNum]].heartrate_bpm[heartbeat]);
      }

    }
  }

  // heartbeat data to chart data

  for (let i = 0; i < 4; i++) {
    const modifiedLabels = astronaut_Heartbeat_Data[i].map((_, index) => {
      return (index % 360 === 0) ? `day ${index / 360}` : '';
    });

    //console.log("Modified labels: " + modifiedLabels);
    //console.log("Astronaut " + i + " has " + astronaut_Heartbeat_Data[i].length + " heartbeats");

    astronaut_Heartbeats_Chartdata[i] = {
      labels: modifiedLabels,
      datasets: [{
      label: 'Astronaut ' + (i + 1) + '\'s Heartbeats',
      data: astronaut_Heartbeat_Data[i],
      borderWidth: 1,
      borderColor: 'rgba(75,192,192,1)',
      backgroundColor: 'rgba(75,192,192,0.2)',
      }]
    };
  }

  /*for (let i = 0; i < 4; i++) {
    let astronaut_data = [];
    let numHeartbeats = healthData[i].heartrate_bpm.length;
    for (let j = 0; j < numHeartbeats; j++) {
      astronaut_data.push(healthData[i].heartrate_bpm[j]);
    }
    astronaut_Heartbeat_Data.push(astronaut_data);
  }*/

  // Start the sleep data transfer from the json file

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

  //console.log(healthData[0][astronaut_dict[0]].heartrate_bpm);
  for (let day = 0; day < healthData.length; day++) {
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      // append the data
      console.log(healthData[day][astronaut_dict[astronautNum]].previous_night_awake_minutes)
      console.log(healthData[day][astronaut_dict[astronautNum]].previous_night_light_minutes)
      console.log(healthData[day][astronaut_dict[astronautNum]].previous_night_deep_minutes)
      console.log(healthData[day][astronaut_dict[astronautNum]].previous_night_rem_minutes)
      astronaut_Sleep_Data[astronautNum][0].push(healthData[day][astronaut_dict[astronautNum]].previous_night_awake_minutes);
      astronaut_Sleep_Data[astronautNum][1].push(healthData[day][astronaut_dict[astronautNum]].previous_night_light_minutes);
      astronaut_Sleep_Data[astronautNum][2].push(healthData[day][astronaut_dict[astronautNum]].previous_night_deep_minutes);
      astronaut_Sleep_Data[astronautNum][3].push(healthData[day][astronaut_dict[astronautNum]].previous_night_rem_minutes);
    }
  }

  // sleep data to chart data

  for (let i = 0; i < 4; i++) {
    const dayLabels = astronaut_Sleep_Data[i][0].map((_, index) => {
      return `day ${index+1}`;
    });

    console.log("Modified labels: " + dayLabels);
    console.log("Astronaut " + i + " has " + (astronaut_Sleep_Data[i][0].length) + " days of sleep data");
    console.log(astronaut_Sleep_Data[i]);

    for (let j = 0; j < 4; j++) {
      astronaut_Sleep_Chartdata[i][j] = {
        labels: dayLabels,
        datasets: [{
          label: 'Astronaut ' + (i + 1) + '\'s Sleep',
          data: astronaut_Sleep_Data[i][j],
          borderWidth: 1,
          borderColor: 'rgba(75,192,192,1)',
          backgroundColor: 'rgba(75,192,192,0.2)',
        }]
      };
    }
  }

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
