import { useEffect, useState } from 'react';
import './Card.module.css'

export default function Card({ cardTitle }) {
  const [value, setValue] = useState(0);
  useEffect(() => {
    setValue
  })
  const formatedValue = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
  return (
    <div>
      <h3>{cardTitle}</h3>
      <p>{formatedValue}</p>
    </div>
  );
}