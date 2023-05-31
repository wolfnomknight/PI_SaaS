import Card from './Card';
import './Section.module.css'

export default function CardSection({ transactions }) {
    const income = transactions.find(obj => obj.income) ? transactions.filter(v => v.income).map(obj => parseFloat(obj.valor)).reduce((acc, v) => acc + v) : 0
    const expense = transactions.find(obj => !obj.income) ? - Math.abs(transactions.filter(v => !v.income).map(obj => parseFloat(obj.valor)).reduce((acc, v) => acc + v)) : 0
    const total = income + expense
    return (
        <section>
            <Card cardTitle={'Entrada'} value={income} />
            <Card cardTitle={'Saída'} value={expense} />
            <Card cardTitle={'Total'} value={total} />
        </section>
    );
}