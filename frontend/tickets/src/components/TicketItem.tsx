import React from 'react'
import {Ticket, TicketItemProps} from '../types';



const TicketItem = ({ticket}: TicketItemProps) => {
  return (
     <tr>
        <td>{ticket.first_name} {ticket.last_name}</td>
        <td>{ticket.email}</td>
        <td>{ticket.issue}</td>
        <td>
            <span className={`priority-${ticket.priority}`}>
                {ticket.priority}
            </span>
        </td>
        <td>
            <span className="action-btn edit">Edit</span>
            <span className="action-btn delete">Delete</span>
        </td>
    </tr>
  )
}

export default TicketItem