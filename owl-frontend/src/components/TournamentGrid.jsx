import React from "react";
import { DataGrid } from "@mui/x-data-grid";
import { Box, Typography } from "@mui/material";

const columns = [
  { field: "id", headerName: "ID", width: 90 },
  { field: "firstName", headerName: "First name", width: 150, editable: true },
  { field: "lastName", headerName: "Last name", width: 150, editable: true },
  {
    field: "age",
    headerName: "Age",
    type: "number",
    width: 110,
    editable: true,
  },
  {
    field: "fullName",
    headerName: "Full name",
    description: "This column has a value getter",
    sortable: false,
    width: 160,
  },
];

const rows = [
  { id: 1, lastName: "Snow", firstName: "Jon", age: 35 },
  { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
  { id: 3, lastName: "Stark", firstName: "Arya", age: 16 },
  { id: 4, lastName: "Targaryen", firstName: "Daenerys", age: 28 },
  { id: 5, lastName: "Melisandre", firstName: "", age: 150 },
  { id: 6, lastName: "Clifford", firstName: "Ferrara", age: 44 },
  { id: 7, lastName: "Frances", firstName: "Rossini", age: 36 },
  { id: 8, lastName: "Roxie", firstName: "Harvey", age: 65 },
];

const TournamentGrid = () => {
  return (
    <Box sx={{ height: 400, width: "100%" }}>
      <Typography variant="h6" gutterBottom>
        User Data
      </Typography>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
        disableSelectionOnClick
        experimentalFeatures={{ newEditingApi: true }}
      />
    </Box>
  );
};

export default TournamentGrid;
