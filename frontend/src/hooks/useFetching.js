import { useState } from "react";

const useFetching = (callback) => {
    const [isLoading,setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const fetching = async () => {
        try {
            setIsLoading(true);
            await callback();

        } catch (e) {

             setError(e);

        } finally {
            setIsLoading(false);
        }
    }

    return [fetching, isLoading, error, setError];
}

export default useFetching;