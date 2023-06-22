import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';
import morgan from 'morgan';
import cors from 'cors';
const app: Express = express();

dotenv.config();

app.use(express.json());
app.use(cors());
app.use(morgan('dev'));

app.get('/', (req: Request, res: Response) => {
  res.send('deneme');
});
app.listen(1234, () => {
  console.log(`[server]: Server is running at http://localhost:${1234}`);
});
