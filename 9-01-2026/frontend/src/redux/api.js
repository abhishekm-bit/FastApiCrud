import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const syllabusApi = createApi({
  reducerPath: "syllabusApi",
  baseQuery: fetchBaseQuery({
baseUrl: process.env.REACT_APP_API_URL || "http://127.0.0.1:8000"

  }),
  endpoints: (builder) => ({
    generateSyllabus: builder.mutation({
      query: (data) => ({
        url: "/api/generate",
        method: "POST",
        body: data
      })
    })
  })
});

export const { useGenerateSyllabusMutation } = syllabusApi;
