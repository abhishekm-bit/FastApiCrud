import { Container, Typography } from "@mui/material";
import SyllabusForm from "./components/SyllabusForm";

function App() {
  return (
    <Container maxWidth="md" sx={{ mt: 5 }}>
      <Typography variant="h4" align="center" gutterBottom>
        🎓 AI Syllabus Generator
      </Typography>

      <SyllabusForm />
    </Container>
  );
}

export default App;
