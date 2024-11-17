import React, { useState } from 'react';
import Header from './components/header.js';
import Heartbeat from './components/Heartbeat.js';
import Sleep from './components/Sleep.js';
import FoodTable from './components/Food.js';
import Other from './components/Other.js';
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
import healthData from "./testing_data.json";
import predictions from "./predictions.json";

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
      return (index % 360 === 0) ? `day ${index / 360 - 6}` : '';
    });

    const pointColors = astronaut_Heartbeat_Data[i].map((_, index) => index > astronaut_Heartbeat_Data[i].length - 360 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)');
    const BKpointColors = astronaut_Heartbeat_Data[i].map((_, index) => index > astronaut_Heartbeat_Data[i].length - 360 ? 'rgba(255,0,0,0.2)' : astronaut_dict_color[i] + '0.2)');

    astronaut_Heartbeats_Chartdata[i] = {
      labels: modifiedLabels,
      datasets: [{
        label: 'Astronaut ' + (i + 1) + '\'s Heart Rate',
        data: astronaut_Heartbeat_Data[i],
        borderWidth: 1,
        borderColor: pointColors,
        backgroundColor: BKpointColors,
        pointBackgroundColor: pointColors,
        segment: {
          borderColor: (ctx) => ctx.p0DataIndex >= astronaut_Heartbeat_Data[i].length - 360 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)',
        }
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
      return `day ${index - 6}`;
    });

    for (let j = 0; j < 4; j++) {
      const sleepTypes = ['Awake', 'Light', 'Deep', 'REM'];

      const pointColors = astronaut_Sleep_Data[i][j].map((_, index) => index > astronaut_Sleep_Data[i][j].length - 2 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)');
      const BKpointColors = astronaut_Sleep_Data[i][j].map((_, index) => index > astronaut_Sleep_Data[i][j].length - 2 ? 'rgba(255,0,0,0.2)' : astronaut_dict_color[i] + '0.2)');

      astronaut_Sleep_Chartdata[i][j] = {
        labels: dayLabels,
        datasets: [{
          label: sleepTypes[j] + ' Sleep in Minutes',
          data: astronaut_Sleep_Data[i][j],
          borderWidth: 1,
          borderColor: pointColors,
          backgroundColor: BKpointColors,
          pointBackgroundColor: BKpointColors,
          segment: {
            borderColor: (ctx) => ctx.p0DataIndex >= astronaut_Sleep_Data[i].length + 4 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)',
          }
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

function processExtrasData(healthData) {
  // this function will be used to take every other data point from the json file and put it into a chart
  // First, find the names of the keys in the json file
  let keys = Object.keys(healthData[0][astronaut_dict[0]]);
  
  // Next, remove the keys that have already been processed
  let keysToRemove = ['heartrate_bpm', 'previous_night_awake_minutes', 'previous_night_light_minutes', 'previous_night_deep_minutes', 'previous_night_rem_minutes', 'meal_1_breakfast', 'meal_2_breakfast', 'meal_3_breakfast', 'meal_1_lunch', 'meal_2_lunch', 'meal_3_lunch', 'meal_1_dinner', 'meal_2_dinner', 'meal_3_dinner'];
  keys = keys.filter(key => !keysToRemove.includes(key));

  // remove "_morning" and "_evening" from the keys
  keys = keys.map(key => key.replace('_morning', '').replace('_evening', ''));

  // remove duplicates from the keys
  keys = keys.filter((value, index, self) => self.indexOf(value) === index);

  // create the data array
  let astronaut_Extras_Data = [];
  let astronaut_Extras_Chartdata = [];

  // loop through the keys and add the data to the array
  for (let day = 0; day < healthData.length; day++) {
    for (let astronautNum = 0; astronautNum < 4; astronautNum++) {
      for (let key of keys) {
        if (!astronaut_Extras_Data[astronautNum]) {
          astronaut_Extras_Data[astronautNum] = [];
        }

        // add the data to the array, sorting the data into the correct key
        if (!astronaut_Extras_Data[astronautNum][key]) {
          astronaut_Extras_Data[astronautNum][key] = [];
        }
        astronaut_Extras_Data[astronautNum][key].push(healthData[day][astronaut_dict[astronautNum]][key + '_morning']*10);
        astronaut_Extras_Data[astronautNum][key].push(healthData[day][astronaut_dict[astronautNum]][key + '_evening']*10);
      }
    }
  }

  console.log(astronaut_Extras_Data);

  // loop through the data and create the chart data
  for (let i = 0; i < 4; i++) {
    astronaut_Extras_Chartdata[i] = [];
    for (let key of keys) {
      const dayLabels = astronaut_Extras_Data[i][key].map((_, index) => {
        return (index % 2 === 0) ? `day ${index / 2 - 6}` : '';
      });

      const pointColors = astronaut_Extras_Data[i][key].map((_, index) => index > astronaut_Extras_Data[i][key].length - 3 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)');
      const BKpointColors = astronaut_Extras_Data[i][key].map((_, index) => index > astronaut_Extras_Data[i][key].length - 3 ? 'rgba(255,0,0,0.2)' : astronaut_dict_color[i] + '0.2)');

      astronaut_Extras_Chartdata[i].push({
        labels: dayLabels,
        datasets: [{
          label: key.replace('_', ' ').replace(/\b\w/g, char => char.toUpperCase()) + " 1-10",
          data: astronaut_Extras_Data[i][key],
          borderWidth: 1,
          borderColor: pointColors,
          backgroundColor: BKpointColors,
          pointBackgroundColor: BKpointColors,
          segment: {
            borderColor: (ctx) => ctx.p0DataIndex >= astronaut_Extras_Data[i][key].length - 2 ? 'rgba(255,0,0,1)' : astronaut_dict_color[i] + '1)',
          }
        }]
      });
    }
  }


  return astronaut_Extras_Chartdata;
}

export default function App() {

  // get the day difference from the url parameters
  const urlParams = new URLSearchParams(window.location.search);
  const dayDifference = parseInt(urlParams.get('day')) || 0;

  // if the day difference is positive, set it to 0
  if (dayDifference > 0) {
    window.location.search = "?day=0";
    dayDifference = 0;
  }

  // retrieve the health data from the json file to ensure that the data is up to date
  const newHealthData = require("./testing_data.json");

  if (newHealthData.length !== healthData.length) {
    healthData = newHealthData;
  }

  // let the max number of days be 7, and cut off the start of the data if it is longer than 7 days
  let max = 7;
  if (healthData.length > max)
    healthData = healthData.slice(healthData.length - max + dayDifference, healthData.length + dayDifference);

  // append the last prediction to the health data
  healthData.push(predictions[predictions.length - 1 + dayDifference]);

  const [formParams, setFormParams] = useState({
    astronaut: '',
  });

  const handleButtonClick = (astronaut) => {
    setFormParams({ astronaut });
  }

  const handlePageChange = (pageDiff) => {
    /*healthData = newHealthData;
    setDayDifference(dayDifference + pageDiff);
    console.log("Page difference: ", dayDifference);
    if (dayDifference < 0) {
      healthData = newHealthData.slice(newHealthData.length - 7 + dayDifference, newHealthData.length + dayDifference);
    } else if (dayDifference > 0 && newHealthData.length > 7 + dayDifference) {
      healthData = newHealthData.slice(newHealthData.length - 7 - dayDifference, newHealthData.length - dayDifference);
    } else {
      healthData = newHealthData.slice(newHealthData.length - 7, newHealthData.length);
    }

    // append the last prediction to the health data. Include the difference in the index
    healthData.push(predictions[predictions.length - 1 + dayDifference]);*/

    // set the url parameters to the page difference
    window.location.search = `?day=${pageDiff + dayDifference}`;
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

  // Start the extras data transfer from the json file

  const astronaut_Extras_Chartdata = processExtrasData(healthData);

  return (
    <div>
      <Header />
      {/* Heartbeat Charts */}
      <div className="container-fluid">
        <div className="row" style={{ minHeight: '200px' }}>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[0]} text={""} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[1]} text={""} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[2]} text={""} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={astronaut_Heartbeats_Chartdata[3]} text={""} />
          </div>
          {/* Food Tables */}
          <div className="col-md-3">
            <FoodTable astronautFoodData={astronaut_Food_Data[0]} headerNumber={1} />
          </div>
          <div className="col-md-3">
            <FoodTable astronautFoodData={astronaut_Food_Data[1]} headerNumber={2} />
          </div>
          <div className="col-md-3">
            <FoodTable astronautFoodData={astronaut_Food_Data[2]} headerNumber={3} />
          </div>
          <div className="col-md-3">
            <FoodTable astronautFoodData={astronaut_Food_Data[3]} headerNumber={4} />
          </div>
        </div>
        
      </div>
      {/* Buttons */}
      <hr style={{ border: '2px solid black', margin: '20px 0' }} />
      <div className="button-container" style={{ textAlign: 'center', margin: '20px 0' }}>
        <button className="btn btn-outline-dark" style={{ position: 'absolute', left: '10px' }} onClick={() => handlePageChange(-1)}>&larr;</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(1)}>1</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(2)}>2</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(3)}>3</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => handleButtonClick(4)}>4</button>
        <button className="btn btn-outline-dark" style={{ position: 'absolute', right: '10px' }} onClick={() => handlePageChange(1)}>&rarr;</button>
      </div>
      <div className="text-box" style={{ textAlign: 'center', margin: '20px 0' }}>
        <input type="text" value={"Astronaut " + formParams.astronaut + ":"} readOnly className="form-control text-center" />
      </div>
      {/* Sleep Charts */}
      <div className="container-fluid">
        {formParams.astronaut && astronaut_Sleep_Chartdata[parseInt(formParams.astronaut) - 1] && (
          <div className="row justify-content-center" style={{ minHeight: '200px' }}>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][1]} text={"Light"} />
            </div>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][2]} text={""} />
            </div>
            <div className="col-md-3 chart-container">
              <Sleep data={astronaut_Sleep_Chartdata[parseInt(formParams.astronaut-1)][3]} text={""} />
            </div>
          </div>
        )}
        {/* Etc. Charts */}
        {formParams.astronaut && astronaut_Extras_Chartdata[parseInt(formParams.astronaut) - 1] && (
          <div className="row justify-content-center" style={{ minHeight: '200px' }}>
            {astronaut_Extras_Chartdata[parseInt(formParams.astronaut) - 1].map((data, index) => (
              <div className="col-md-3 chart-container" key={index}>
                <Other data={data} text={""} />
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
