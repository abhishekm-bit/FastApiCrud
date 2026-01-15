import { configureStore } from "@reduxjs/toolkit";
import { syllabusApi } from "./api";

export const store = configureStore({
  reducer: {
    [syllabusApi.reducerPath]: syllabusApi.reducer
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(syllabusApi.middleware)
});
