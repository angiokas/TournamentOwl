import React from "react";
import {
  AppBar,
  Toolbar,
  Button,
  Box,
  BottomNavigation,
  Typography,
  Link,
  Container,
} from "@mui/material";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import RestoreIcon from "@mui/icons-material/Restore";
import FavoriteIcon from "@mui/icons-material/Favorite";
import LocationOnIcon from "@mui/icons-material/LocationOn";

import { useNavigate } from "react-router-dom";

const PageLayout = ({ pages, children }) => {
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
      <AppBar>
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

  function BottomNav() {
    const [value, setValue] = React.useState(0);

    return (
      <Box sx={{ width: 500 }}>
        <BottomNavigation
          showLabels
          value={value}
          onChange={(event, newValue) => {
            setValue(newValue);
          }}
        >
          <BottomNavigationAction label="Recents" icon={<RestoreIcon />} />
          <BottomNavigationAction label="Favorites" icon={<FavoriteIcon />} />
          <BottomNavigationAction label="Nearby" icon={<LocationOnIcon />} />
        </BottomNavigation>
      </Box>
    );
  }

  return (
    <Box
      display="flex"
      flexDirection="column"
      minHeight="100vh"
      maxWidth="100%"
    >
      <NavigationBar pages={pages} />
      <Toolbar />

      <Box component="main" flexGrow={1} padding={8}>
        <Container>{children}</Container>
      </Box>

      <BottomNav />
    </Box>
  );
};

export default PageLayout;
