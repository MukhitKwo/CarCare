import { useEffect, useState } from 'react';
import axios from 'axios';

function CarList() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    axios.get('/api/carinfo/')
      .then(response => {
        setCars(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      {cars.map(car => (
        <div key={car.id}>
          {car.brand} {car.model} - {car.year}
        </div>
      ))}
    </div>
  );
}

export default CarList;
