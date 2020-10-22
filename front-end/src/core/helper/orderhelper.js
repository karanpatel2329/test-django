import {API} from '../../backend';

export const CreateOrder = (userId, token, orderData) =>{
    const formData = new FormData();

    for(const name in orderData){
        formData.append(name,orderData[name]);
    }

    return fetch(`${API}order/add/${userId}/${token}/`, {
        method:"POST",
        body:formData
    })
    .then(response=>{
        return response.json();
    })
    .catch(err=>console.log(err))
}




