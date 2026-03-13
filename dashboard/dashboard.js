import axios from "axios"
import { useEffect, useState } from "react"

function Dashboard(){

const [alerts,setAlerts]=useState([])

useEffect(()=>{

axios.get("http://localhost:8000/alerts")
.then(res=>setAlerts(res.data))

},[])

return(

<div>

<h1>AI IDS Dashboard</h1>

{alerts.map((a,i)=>

<div key={i}>
Attack Detected: {a.type}
</div>

)}

</div>

)

}

export default Dashboard