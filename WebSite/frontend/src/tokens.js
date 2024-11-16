import axios from "axios";

const getToken = async (userData) => {
    axios.post(`http://127.0.0.1:8000/api/Tokens`, userData, {
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(res => {
        console.log('Success:', res.data)
    .then(data =>{
        const accessToken = data.access_token;
        const refreshToken = data.refresh_token;
        localStorage.setItem('accessToken', accessToken);
        document.cookie = `refreshToken=${refreshToken}; HttpOnly; Secure; SameSite=Strict`;
    }) 
        // Redirect or show success message
    })
    .catch(error => {
        console.log('Error response:', error.response?.data); // Debug log
        console.log('Error status:', error.response?.status);
        console.log('Error headers:', error.response?.headers);
    });
};

export default getToken;