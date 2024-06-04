const api_url = "http://127.0.0.1:8000";  // http://127.0.0.1:8000  для запуска вне докера // для запуска в докере ""
// //http://127.0.0.1:8000
// //http://restapimob

// PROD

export const api_get_vacancy = `${api_url}/api/vacancy/`;
// // /api/v1/start_parsing/
// // /practice/getVacancy.php

export const api_parse = `${api_url}/api/start_parsing/`;
// // /api/v1/start_parsing/
// // /queries/saveDescription.php


// // DEV
// //
// const api_url = "http://restapimob";
// // http://127.0.0.1:8000
// // http://restapimob
// //
// export const api_get_vacancy = `${api_url}/practice/getVacancy.php`;
// // /api/v1/calendar/days_summary/
// // /practice/getVacancy.php
// //
// export const api_parse = "/queries/saveDescription.php";
// // /api/v1/calendar/days_summary/
// // /queries/saveDescription.php