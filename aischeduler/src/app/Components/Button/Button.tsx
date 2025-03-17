'use client'

import axios from "axios";
import styles from "./button.module.scss";

const Button = () => {
    const execute = () => {
        axios.get('http://localhost:8000/').then((response: any) => {
          alert(JSON.stringify(response.data))
        })
      }

    return (
        <button className="button" onClick={execute}>Click me</button>
    )
}

export default Button