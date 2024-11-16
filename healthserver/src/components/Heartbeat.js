import React from 'react';
import { Line } from 'react-chartjs-2';

const Heartbeat = ({ options, data }) => {
    return (
        <Line options={options} data={data} />
    );
};

export default Heartbeat;