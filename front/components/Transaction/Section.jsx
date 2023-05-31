import { useState } from "react";
import { createPortal } from "react-dom"
import Button from "../Button";
import Modal from "./Modal"

export default function TransactionSection({ setTransactions }) {
    const [isOpen, setIsOpen] = useState(false)
    return (
        <section>
            <Button onClick={() => setIsOpen(true)}>Adicionar Transação</Button>
            {isOpen && createPortal(<Modal isOpen={isOpen} onClose={() => setIsOpen(false)} setTransactions={setTransactions} />, document.body)}
        </section>
    );
}