import CardSection from '../components/Cards/Section';
import TableSection from '../components/Table/Section';
import TransactionSection from '../components/Transaction/Section';
import './home.module.css'

export default function Home() {
  return (
    <main>
      <h1>Homepage</h1>
      <CardSection />
      <TransactionSection />
      <TableSection />
    </main>
  );
}