import Card from '../components/Card';
import styles from './home.module.css'

export default function Home() {
  return (
    <main>
      <h1>Homepage</h1>
      <Card cardTitle={'Entrada'} />
    </main>
  );
}