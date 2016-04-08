
class MainController {
  
  constructor() {
    this.name = this.getDate();
    this.result = "Sources: New York Times, Washington Post, The Guardian, Reuters, Fox News, UPI World News, CNN, ABC News";
  }

  getDate() {
    const today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1;
    const yyyy = today.getFullYear();

    if (dd < 10) {
      dd = '0' + dd;
    }
    if (mm < 10) {
      mm = '0' + mm;
    }
    return mm + "/" + dd + "/" + yyyy + " Headlines";
  }
}

export default MainController;

