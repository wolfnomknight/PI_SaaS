import { useRef, useEffect } from 'react'
import './Modal.module.css'

export default function Modal({ isOpen, onClose }) {
    const ref = useRef(null);
    useEffect(() => {
        if (isOpen) {
            ref.current?.showModal()
            return () => ref.current?.close()
        }
    }, [isOpen]);

    const dt = new Date().toISOString()
    return (
        <dialog ref={ref}> 
            <form method="dialog" onSubmit={onClose}>
                <fieldset>
                    <label>
                        Titulo
                        <input type="text" />
                    </label>
                    <label>
                        Entrada
                        <input name="income-expense" type="radio" />
                    </label>
                    <label>
                        Despesa
                        <input name="income-expense" type="radio" />
                    </label>
                    <label>
                        Valor
                        <input type="number" />
                    </label>
                    <label>
                        <input type="hidden" value={dt}/>
                    </label>
                </fieldset>
                <button type="button" onClick={onClose}>Cancelar</button>
                <button type="submit">Salvar</button>
            </form>
        </dialog>
    )
}