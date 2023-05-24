import { useEffect, useState } from 'react';
import {data} from '../testdata';
import TicketItem from './TicketItem';
import {Ticket} from '../types';



const TicketList = () => {
    const [tickets, setTickets] = useState<Ticket[]>();

    useEffect(()=>{
        const doFetch = async() => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/tickets');
                const data: Ticket[] = await response.json();
                setTickets(data);
                
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }

        doFetch();
    },[]); 

  return (
    <div>
        <h2 className="page-title">Current Tickets</h2>
        <table className="table table-bordered">
            <thead>
                <tr>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Issue</th>
                <th scope="col">Priority</th>
                <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
            {tickets?.map((item: Ticket, i: number) => <TicketItem key={i} ticket={item} />)}
            </tbody> 
        </table>   
    </div>
  )
}

export default TicketList;