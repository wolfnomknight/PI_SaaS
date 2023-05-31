import './Card.module.css'

export default function Card({ cardTitle, value }) {
  const formatedValue = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
  return (
    <div>
      <h3>{cardTitle}</h3>
      <p>{formatedValue}</p>
    </div>
  );
}