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

export const data = {
  labels,
  datasets: [{
    label: '# of Votes',
    data: [120, 190, 70, 50, 80, 90],
    borderWidth: 1,
    borderColor: 'rgba(75,192,192,1)',
    backgroundColor: 'rgba(75,192,192,0.2)',
  }]
};

export default function App() {
  const [formParams, setFormParams] = useState({
    astronaut: '',
  });

  const handleButtonClick = (astronaut) => {
    setFormParams({ astronaut });
  }

  return (
    <div>
      <Header />
      <div className="container-fluid" style={{ padding: "5px" }}>
        <div className="row" style={{ minHeight: '200px' }}>
          <div className="col-md-3 chart-container">
            <Heartbeat data={data} text={"Heartbeat of Astronaut 1"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={data} text={"Heartbeat of Astronaut 2"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={data} text={"Heartbeat of Astronaut 3"} />
          </div>
          <div className="col-md-3 chart-container">
            <Heartbeat data={data} text={"Heartbeat of Astronaut 4"} />
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
        <div className="row justify-content-center" style={{ minHeight: '200px' }}>
          <div className="col-md-3 chart-container">
            <Sleep data={data} text={"Amount of light sleep"} />
          </div>
          <div className="col-md-3 chart-container">
            <Sleep data={data} text={"Amount of heavy sleep"} />
          </div>
          <div className="col-md-3 chart-container">
            <Sleep data={data} text={"Amount of REM sleep"} />
          </div>
        </div>
      </div>
    </div>
  );
}
