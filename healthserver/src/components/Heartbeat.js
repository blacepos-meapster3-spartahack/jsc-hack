import React from 'react';
import { Line } from 'react-chartjs-2';

const Heartbeat = ({ options, data }) => {
    return (
        <div className="container-fluid" style={{ padding: "5px" }}>
            <div className="row" style={{ minHeight: '200px' }}>
                <div className="col-md-3 chart-container">
                    <Line options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Line options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Line options={options} data={data} />
                </div>
                <div className="col-md-3 chart-container">
                    <Line options={options} data={data} />
                </div>
            </div>
        </div>
    );
};

export default Heartbeat;