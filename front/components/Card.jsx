import Img from "./Img";

export default function Card({ cardTitle }) {
  return (
    <div>
      <h3>{cardTitle}</h3>
      <p>Valor: 0,00</p>
      <Img name={'plus'} />
    </div>
  );
}