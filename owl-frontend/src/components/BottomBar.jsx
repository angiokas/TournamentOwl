import React from "react";
import { Box, Typography, Button, Link } from "@mui/material";

const BottomBar = () => {
  return (
    <Box
      sx={{
        position: "fixed",
        bottom: 0,
        width: "100%",
        padding: "1rem",
        textAlign: "center",
      }}
    >
      <Typography variant="body2">
        <Button
          variant="contained"
          color="primary"
          sx={{ marginRight: "1rem" }}
          component={Link}
          href="mailto:someone@example.com"
        >
          Contact Me
        </Button>
        <Button
          variant="contained"
          color="secondary"
          sx={{ marginRight: "1rem" }}
          component={Link}
          href="https://www.paypal.com/donate?hosted_button_id=EXAMPLE"
        >
          Donate
        </Button>
      </Typography>
      <Typography variant="body2">
        © {new Date().getFullYear()} TournamentOwl. Licensed under the{" "}
        <Link
          href="https://www.gnu.org/licenses/gpl-3.0.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          GNU General Public License v3.0
        </Link>
        .
      </Typography>
    </Box>
  );
};

export default BottomBar;
