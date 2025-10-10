const { Builder, By, until } = require('selenium-webdriver');
const { expect } = require('chai');

describe('SauceDemo E2E Test', function() {
  this.timeout(60000);
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  it('should complete purchase flow successfully', async function() {

    await driver.get('https://www.saucedemo.com/');

    await driver.findElement(By.id('user-name')).sendKeys('standard_user');
    await driver.findElement(By.id('password')).sendKeys('secret_sauce');
    await driver.findElement(By.id('login-button')).click();

    await driver.wait(until.elementLocated(By.className('inventory_item')), 10000);

    const itemNameElem = await driver.findElement(By.className('inventory_item_name'));
    const itemPriceElem = await driver.findElement(By.className('inventory_item_price'));
    const itemName = await itemNameElem.getText();
    const itemPrice = await itemPriceElem.getText();

    const addToCartBtn = await driver.findElement(By.xpath("//button[contains(text(),'Add to cart')]"));
    await addToCartBtn.click();

    await driver.findElement(By.className('shopping_cart_link')).click();

    await driver.wait(until.elementLocated(By.className('cart_item')), 10000);
    const cartPrice = await driver.findElement(By.className('inventory_item_price')).getText();

    expect(cartPrice).to.equal(itemPrice);

    await driver.findElement(By.id('checkout')).click();
    await driver.findElement(By.id('first-name')).sendKeys('John');
    await driver.findElement(By.id('last-name')).sendKeys('Doe');
    await driver.findElement(By.id('postal-code')).sendKeys('411001');
    await driver.findElement(By.id('continue')).click();

    const checkoutName = await driver.findElement(By.className('inventory_item_name')).getText();
    const checkoutPrice = await driver.findElement(By.className('inventory_item_price')).getText();

    expect(checkoutName).to.equal(itemName);
    expect(checkoutPrice).to.equal(itemPrice);

    await driver.findElement(By.id('finish')).click();

    const confirmationText = await driver.findElement(By.className('complete-header')).getText();
    expect(confirmationText).to.equal('Thank you for your order!');
  });
});
