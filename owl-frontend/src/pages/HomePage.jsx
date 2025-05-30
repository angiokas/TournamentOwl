import React from "react";
import { useEffect, useState } from "react";

const API_ENDPOINT_URL = "http://127.0.0.1:8000/api/items/";

const HomePage = () => {
  const [items, setItems] = useState([]);

  const fetchData = (url) => {
    fetch(url)
      .then((response) => response.json())
      .then((data) => setItems(data))
      .then((error) => console.error("Error fetching items:", error));
  };
  const url = API_ENDPOINT_URL;

  useEffect(() => fetchData(url), [url]);
  return (
    <div>
      <h1>Welcome to the Home Page</h1>
    </div>
  );
};

export default HomePage;
