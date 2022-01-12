import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// Express App ------------------------------
const app = express();
const port = 1245;

// Redis Client -----------------------------
const client = createClient();
const getAsync = promisify(client.get).bind(client);

// Variables --------------------------------

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// Functions --------------------------------

const getItemById = (id) => {
  return listProducts.find((item) => {
    return item.itemId === parseInt(id);
  });
};

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  return await getAsync(`item.${itemId}`);
};

// Code -------------------------------------

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const stock = await getCurrentReservedStockById(req.params.itemId);
  const item = getItemById(req.params.itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    res.json({
      ...item,
      currentQuantity: item.initialAvailableQuantity - stock,
    });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const stock = await getCurrentReservedStockById(req.params.itemId);
  const item = getItemById(req.params.itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    if (stock >= item.initialAvailableQuantity)
      res.json({ status: 'Not enough stock available', itemId: item.itemId });
    else reserveStockById(item.itemId, stock);
    res.json({ status: 'Reservation confirmed', itemId: item.itemId });
  }
});

app.listen(port);
