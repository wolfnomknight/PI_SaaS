import { useEffect, useState } from 'react';
import CardSection from '../components/Cards/Section';
import TableSection from '../components/Table/Section';
import TransactionSection from '../components/Transaction/Section';
import './home.module.css'

export default function Home() {
  const [transactions, setTransactions] = useState(JSON.parse(localStorage.getItem("transactions")) ?? [])

  return (
    <main>
      <h1>Homepage</h1>
      <CardSection transactions={transactions} />
      <TransactionSection setTransactions={setTransactions} />
      <TableSection transactions={transactions} setTransactions={setTransactions} />
    </main>
  );
}