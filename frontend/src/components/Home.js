import React from "react";
import Button from "@mui/material/Button";
import { Box, Typography } from "@mui/material";
import ItemDetail from "./ItemDetail";

function Home() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <Box textAlign={'center'}>
      <h1>Home</h1>
      <Box>Hello</Box>
      <Button onClick={handleOpen} variant="outlined" color="secondary">
        click
      </Button>
      
      <ItemDetail open={open} handleClose={handleClose} />
    </Box>
  );
}

export default Home;