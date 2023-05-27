import './Section.module.css'
import Card from './Card';

export default function CardSection() {
    return (
        <section>
            <Card cardTitle={'Entrada'} />
            <Card cardTitle={'Saída'} />
            <Card cardTitle={'Total'} />
        </section>
    );
  }