class element():
    #login & logout
    name = "username" #by_name
    password = "password" #by_name
    loginBtn = "orangehrm-login-button" #by_class
    required = "oxd-input-group__message" #by_class
    invalidCred = "oxd-alert--error" #by_class
    loginPage = "orangehrm-login-title" #by_class
    dashboard = "oxd-topbar-header" #by_class
    userProfil = "oxd-userdropdown-tab" #by_class
    logoutBtn = "//a[contains(text(),'Logout')]" #by_xpath

    #add user
    adminBtn = "oxd-main-menu-item" #by_class
    addBtn = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]" #by_xpath
    selectUser = "oxd-select-text--arrow" #by class
    userRole = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span" #by_xpath
    selectStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]" #by_xpath
    enable = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span" #by_xpath
    employee = "oxd-autocomplete-wrapper" #by_class
    hintEmployee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input' #by_xpath
    listEmployee = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span" #by_xpath
    newUsername = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'#by_xpath
    newPassword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input' #by_xpath
    confirmPassword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input' #by_xpath
    saveBtn = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]" #by_xpath

    #invalid / blank user
    existUser = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span" #by_xpath
    blankRole = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/span' #by_xpath
    blankEmployee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/span' #by_xpath
    blankStatus = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/span' #by_xpath
    blankUsername = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span' #by_xpath
    blankPassword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span' #by_xpath
    blankField = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/span" #by_path
    invalidUser = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span' #by_xpath
    invalidPassword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span' #by_xpath
    invalidConfPass = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/span' #by_xpath

    #search user
    usernameSearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    userRoleSearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'
    adminSearch = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span"
    statusSearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'
    enableSearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div/span'
    searchButton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    resetButton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]'
    searchFoundUser = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
    searchNotFoundUser = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
    reset = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'

    #add location
    selectDropdown = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span'
    selectLocations = "//a[contains(text(),'Locations')]"
    addBtnLoc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button'
    nameLoc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'
    city = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
    state = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
    pCode = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input'
    country = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]'
    phone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input'
    fax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/div[2]/input'
    address = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea'
    notes = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[8]/div/div[2]/textarea'
    saveBtnLoc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'
    cancelBtnLoc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]'

    #search location
    nameSearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    citySearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    countrySearch = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
    searchBtn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    searchFound = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
    searchNotFound = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'

    #edit location
    editBtn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]'
    cityEdit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
    stateEdit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
    saveEdit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'
    cancelEdit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]'

    #delete location
    deleteBtn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]'
    confirmDelete = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    cancelDelete = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[1]'

    #add job
    jobDropdown = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    jobSelect = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a'
    addJob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div'
    jobTitle = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    jobDesc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea'
    addNote = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea'
    saveJob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]'
    cancelJob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[1]'

class url():
    baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboardUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    logoutUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/logout"
    addUserUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    addLocUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations"
    failedAddLoc = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveLocation"