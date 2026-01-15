import {
  TextField,
  Button,
  MenuItem,
  Card,
  CardContent,
  CircularProgress,
  Typography,
  Box
} from "@mui/material";
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { useGenerateSyllabusMutation } from "../redux/api";

export default function SyllabusForm() {

  const [form, setForm] = useState({
    url: "",
    course: "",
    level: "Beginner",
    duration: "1 Month"
  });

  const [errors, setErrors] = useState("");
  const [output, setOutput] = useState("");

  const [generateSyllabus, { isLoading }] =
    useGenerateSyllabusMutation();

  // URL validation
  const isValidUrl = (url) => {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setErrors("");
  };

  const validateForm = () => {

    if (!form.url) return "URL is required";
    if (!isValidUrl(form.url)) return "Enter valid URL";
    if (!form.course) return "Course name required";
    if (!form.level) return "Select level";
    if (!form.duration) return "Select duration";

    return "";
  };

  const handleSubmit = async () => {

    const err = validateForm();
    if (err) {
      setErrors(err);
      return;
    }

    try {
      const res = await generateSyllabus(form).unwrap();
      setOutput(res.syllabus);
    } catch {
      alert("Backend error!");
    }
  };

  return (
    <>
      <Card sx={{ p: 3 }}>

        <TextField
          fullWidth
          label="Course URL"
          name="url"
          margin="normal"
          value={form.url}
          onChange={handleChange}
        />

        <TextField
          fullWidth
          label="Course Name"
          name="course"
          margin="normal"
          value={form.course}
          onChange={handleChange}
        />

        <TextField
          select
          label="Level"
          name="level"
          fullWidth
          margin="normal"
          value={form.level}
          onChange={handleChange}
        >
          <MenuItem value="Beginner">Beginner</MenuItem>
          <MenuItem value="Intermediate">Intermediate</MenuItem>
          <MenuItem value="Advanced">Advanced</MenuItem>
        </TextField>

        <TextField
          select
          label="Duration"
          name="duration"
          fullWidth
          margin="normal"
          value={form.duration}
          onChange={handleChange}
        >
          <MenuItem value="1 Month">1 Month</MenuItem>
          <MenuItem value="3 Months">3 Months</MenuItem>
          <MenuItem value="6 Months">6 Months</MenuItem>
        </TextField>

        {errors && (
          <Typography color="error" mt={1}>
            {errors}
          </Typography>
        )}

<Button
  fullWidth
  variant="contained"
  sx={{ mt: 2 }}
  onClick={handleSubmit}
  disabled={isLoading}
>
 {isLoading ? "Generating..." : "Generate Syllabus"}
</Button>
      </Card>

      {isLoading && (
        <Box
          display="flex"
          justifyContent="center"
          mt={4}
        >
          <CircularProgress />
        </Box>
      )}

      {output && (
        <Card sx={{ mt: 4 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Generated Syllabus
            </Typography>

            <ReactMarkdown>
              {output}
            </ReactMarkdown>
          </CardContent>
        </Card>
      )}
    </>
  );
}
