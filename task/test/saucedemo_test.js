const { Builder, By, until } = require('selenium-webdriver');
const { expect } = require('chai');

describe('SauceDemo End-to-End Flow', function() {
  this.timeout(60000); // allow enough time for browser operations
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  it('should complete the purchase flow successfully', async function() {
    await driver.get('https://www.saucedemo.com/');

    await driver.findElement(By.id('user-name')).sendKeys('standard_user');
    await driver.findElement(By.id('password')).sendKeys('secret_sauce');
    await driver.findElement(By.id('login-button')).click();

    await driver.wait(until.elementLocated(By.className('inventory_item')), 10000);

    const itemNameElem = await driver.findElement(By.className('inventory_item_name'));
    const itemPriceElem = await driver.findElement(By.className('inventory_item_price'));
    const itemName = await itemNameElem.getText();
    const itemPrice = await itemPriceElem.getText();

    await driver.findElement(By.xpath("//button[contains(text(),'Add to cart')]")).click();

    await driver.findElement(By.className('shopping_cart_link')).click();

    const cartItemPrice = await driver.findElement(By.className('inventory_item_price')).getText();
    expect(cartItemPrice).to.equal(itemPrice);

    await driver.findElement(By.id('checkout')).click();

    await driver.findElement(By.id('first-name')).sendKeys('John');
    await driver.findElement(By.id('last-name')).sendKeys('Doe');
    await driver.findElement(By.id('postal-code')).sendKeys('12345');
    await driver.findElement(By.id('continue')).click();

    const checkoutItemName = await driver.findElement(By.className('inventory_item_name')).getText();
    const checkoutItemPrice = await driver.findElement(By.className('inventory_item_price')).getText();

    expect(checkoutItemName).to.equal(itemName);
    expect(checkoutItemPrice).to.equal(itemPrice);

    await driver.findElement(By.id('finish')).click();
    
    const successMsg = await driver.findElement(By.className('complete-header')).getText();
    expect(successMsg).to.equal('Thank you for your order!');
  });
});
