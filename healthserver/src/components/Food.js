import React from 'react';

const FoodTable = ({ astronautFoodData, headerNumber }) => (
    <div>
        <h3>Astronaut {headerNumber} Food Data</h3>
        <table className="table table-striped table-sm">
            <thead>
                <tr>
                    <th style={{ textAlign: 'center' }}></th>
                    <th style={{ textAlign: 'center' }}>Breakfast</th>
                    <th style={{ textAlign: 'center' }}>Lunch</th>
                    <th style={{ textAlign: 'center' }}>Dinner</th>
                </tr>
            </thead>
            <tbody>
                {astronautFoodData.map((dayData, dayIndex) => (
                    <tr key={dayIndex}>
                        <td style={{ textAlign: 'center' }}>{`Day ${dayIndex + 1}`}</td>
                        <td style={{ textAlign: 'center' }}>{dayData[0]}</td>
                        <td style={{ textAlign: 'center' }}>{dayData[1]}</td>
                        <td style={{ textAlign: 'center' }}>{dayData[2]}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
);

export default FoodTable;