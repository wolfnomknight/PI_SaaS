import Rows from "./Rows";

export default function TableSection({transactions, setTransactions}) {
    return (
        <section>
            <table>
                <thead>
                    <tr>
                        <td>Título</td>
                        <td>Valor</td>
                        <td>Remover</td>
                    </tr>
                </thead>
                <Rows transactions={transactions} setTransactions={setTransactions} />
            </table>
        </section>
    )
}