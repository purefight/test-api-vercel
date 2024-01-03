const express = require('express')
const app = express()
const PORT = 4000

app.listen(PORT, () => {
    console.log(`API Listening on PORT ${PORT}`)
})

app.get('/', (req, res)=> {
    res.send('This in my AIP running...')
}) 

app.get('/about', (req, res)=> {
    res.send('This in my about route')
}) 

module.exports = app