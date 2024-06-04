import axios from "axios";
import { api_get_vacancy,api_parse } from "./config";

axios.defaults.withCredentials = true;

class ApiService {
    static async getVacancy(string) {
        const response = await axios.get(api_get_vacancy, string);

        return response.data.data;
    }

    static async startParse(country="",name="",page_start=0,page_end=0) {
        const response = await axios.get(api_parse, {
            params: {
                country,
                name,
                page_start,
                page_end
            }
        });

        return response.data.data;
    }

}

export default ApiService;
