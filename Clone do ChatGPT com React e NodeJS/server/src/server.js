const app = require("./app")

const port = process.env.PORT || 5000
const dotenv = require("dotenv")

app.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
