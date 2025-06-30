import React, { useState } from "react";

// Sample data for the grid
const sampleData = [
  { id: 1, name: "John Doe", age: 25, country: "USA" },
  { id: 2, name: "Jane Smith", age: 30, country: "Canada" },
  { id: 3, name: "Samuel Green", age: 28, country: "UK" },
  { id: 4, name: "Rachel Adams", age: 35, country: "Australia" },
  { id: 5, name: "Michael Brown", age: 40, country: "Germany" },
];

const TournamentGrid = ({ headers, data }) => {
  const createRow = (items, className) => {
    return (
      <div className={className}>
        {items.map((item, index) => (
          <div key={index} className="cell">
            {item}
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="data-grid">
      <div className="header-row">
        {headers.map((header, index) => (
          <div key={index} className="header-cell">
            {header}
          </div>
        ))}
      </div>

      {data.map((row, index) => (
        <div key={index} className="row">
          {Object.values(row).map((value, idx) => (
            <div key={idx} className="cell">
              {value}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default TournamentGrid;
