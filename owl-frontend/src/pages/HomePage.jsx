import React from "react";
import { useEffect, useState } from "react";

const API_ENDPOINT_URL = "http://127.0.0.1:8000/api/tournaments/";

const HomePage = () => {
  const styles = {
    container: {
      padding: "20px",
      borderRadius: "8px",
      border: "1px solid #ddd",
      backgroundColor: "#f9f9f9",
      marginTop: "20px",
      fontFamily: "monospace",
    },
    pre: {
      whiteSpace: "pre-wrap",
      wordWrap: "break-word",
      fontSize: "16px",
      color: "#333",
    },
  };

  const PrettyJsonDisplay = ({ data }) => {
    if (typeof data !== "object" || data === null) {
      return <p>Invalid JSON data.</p>;
    }

    return (
      <div style={styles.container}>
        <pre style={styles.pre}>{JSON.stringify(data, null, 2)}</pre>
      </div>
    );
  };

  const [items, setItems] = useState([]);

  const fetchData = (url) => {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);
        setItems(data.data);
      })
      .catch((error) => console.error("Error fetching items:", error));
  };
  const url = API_ENDPOINT_URL;

  useEffect(() => fetchData(url), [url]);
  return (
    <div>{items ? <PrettyJsonDisplay data={items} /> : <p>Loading...</p>}</div>
  );
};

export default HomePage;
