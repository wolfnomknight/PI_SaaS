import Button from "../Button";

export default function Rows({ transactions, setTransactions }) {
    function removeTransaction(idx) {
        transactions.splice(idx, 1)
        localStorage.setItem("transactions", JSON.stringify(transactions))
        setTransactions(JSON.parse(localStorage.getItem("transactions")))
    }
    return (
        <tbody>
            {transactions.map((obj, idx) => {
                return (
                    <tr key={idx}>
                        <td>{obj.titulo}</td>
                        <td>{obj.valor}</td>
                        <td>
                            <Button onClick={removeTransaction}>Remover</Button>
                        </td>
                    </tr>
                )
            })}
        </tbody> 
    )
}