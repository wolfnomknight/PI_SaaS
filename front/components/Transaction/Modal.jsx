import { useRef, useEffect } from 'react'
import './Modal.module.css'
import Button from '../Button';

export default function Modal({ isOpen, onClose, setTransactions }) {
    const ref = useRef(null);
    useEffect(() => {
        if (isOpen) {
            ref.current?.showModal()
            return () => ref.current?.close()
        }
    }, [isOpen]);
    function handleSubmit(e) {
        e.preventDefault()
        const transactionData = new FormData(e.target)
        const transactions = JSON.parse(localStorage.getItem("transactions")) ?? []
        transactions.push(Object.fromEntries(transactionData.entries()))
        localStorage.setItem("transactions", JSON.stringify(transactions))
        setTransactions(JSON.parse(localStorage.getItem("transactions")))
        onClose()
    }
    return (
        <dialog ref={ref}> 
            <form method="dialog" onSubmit={handleSubmit}>
                <fieldset>
                    <label>
                        Titulo
                        <input name="titulo" type="text"  required/>
                    </label>
                    <label>
                        Entrada
                        <input name="income" type="checkbox" defaultChecked />
                    </label>
                    <label>
                        Valor
                        <input name="valor" type="number" step="0.01" required/>
                    </label>
                </fieldset>
                <Button onClick={onClose}>Cancelar</Button>
                <Button type="submit">Salvar</Button>
            </form>
        </dialog>
    )
}