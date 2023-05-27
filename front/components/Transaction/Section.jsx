import { useState } from "react";
import { createPortal } from "react-dom"
import Button from "./Button";
import Modal from "./Modal"

export default function TransactionSection() {
    const [isOpen, setIsOpen] = useState(false)
    return (
        <section>
            <Button onOpen={() => setIsOpen(true)} />
            {isOpen && createPortal(<Modal isOpen={isOpen} onClose={() => setIsOpen(false)} />, document.body)}
        </section>
    );
}