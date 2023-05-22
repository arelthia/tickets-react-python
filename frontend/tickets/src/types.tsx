export enum Priority {
    low = "low",
    medium = "medium",
    high = "high"
  };
  
  
  export type Ticket = {
    id: string,
    first_name: string,
    last_name: string,
    email: string,
    issue: string,
    priority?: string,
  };


  export type TicketItemProps ={
    key: number,
    ticket: Ticket
};