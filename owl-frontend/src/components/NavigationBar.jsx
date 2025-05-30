import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Router, Navigate, useNavigate } from "react-router-dom";

const buttonStyles = {
  fontSize: "1.1rem",
  fontWeight: "bold",
  marginRight: "10px",
};

const NavigationBar = ({ pages }) => {
  const navigate = useNavigate();
  const handleClick = (route) => {
    navigate(route);
  };
  return (
    <AppBar position="fixed">
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
        {pages.map((page) => (
          <Button
            key={`button_${page.name}`}
            color="inherit"
            sx={buttonStyles}
            onClick={() => handleClick(page.route)}
          >
            {page.title}
          </Button>
        ))}
      </Toolbar>
    </AppBar>
  );
};

export default NavigationBar;
