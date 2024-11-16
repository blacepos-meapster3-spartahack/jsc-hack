import React, { useState } from 'react';
import Header from './components/header.js';
import Heartbeat from './components/Heartbeat.js';
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

export const options = {
  responsive: true,
  aspectRatio: 1.5, // Adjust this value to change the aspect ratio
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Heatbeats',
    },
  },
  scales: {
    y: {
      beginAtZero: true
    },
  }
};

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
  const [text, setText] = useState('');

  return (
    <div>
      <Header />
      <div className="container-fluid" style={{ padding: "5px" }}>
            <div className="row" style={{ minHeight: '200px' }}>
                <div className="col-md-3 chart-container">
                    <Heartbeat options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Heartbeat options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Heartbeat options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Heartbeat options={options} data={data} />
                </div>
            </div>
        </div>
      <hr style={{ border: '2px solid black', margin: '20px 0' }} />
      <div className="button-container" style={{ textAlign: 'left', margin: '20px 0' }}>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => setText('Astronaut 1 Selected')}>1</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => setText('Astronaut 2 Selected')}>2</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => setText('Astronaut 3 Selected')}>3</button>
        <button className="btn btn-outline-dark" style={{ margin: '0 0.1%' }} onClick={() => setText('Astronaut 4 Selected')}>4</button>
      </div>
      <div className="text-box" style={{ textAlign: 'center', margin: '20px 0' }}>
        <input type="text" value={text} readOnly className="form-control" />
      </div>
    </div>
  );
}
