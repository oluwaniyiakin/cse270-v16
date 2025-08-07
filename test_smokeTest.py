{
  "id": "da5d8c4f-c226-4ed3-b66b-5e0e8fde0209",
  "version": "2.0",
  "name": "Smoke Test",
  "url": "http://127.0.0.1:5500/teton/1.6/index.html",
  "tests": [{
    "id": "c7ee5ded-a2f6-4c8e-b846-4676d8a1667d",
    "name": "Check Site Logo",
    "commands": [{
      "id": "f8e5ba5b-0af4-4e8d-bac5-9bb89b4977e8",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "949c19cc-035c-4799-ae68-8af4453c3658",
      "comment": "",
      "command": "setWindowSize",
      "target": "550x692",
      "targets": [],
      "value": ""
    }, {
      "id": "4ac2f7f8-cdb4-4f2e-b833-8d39991cbcd8",
      "comment": "",
      "command": "click",
      "target": "css=.header-logo img",
      "targets": [
        ["css=.header-logo img", "css:finder"],
        ["xpath=//img[@alt='Teton Chamber of Commerce Logo']", "xpath:img"],
        ["xpath=//div[@id='content']/header/div/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4e3f4e6e-facd-426e-bfa5-c4203259ca76",
      "comment": "",
      "command": "",
      "target": "",
      "targets": [],
      "value": ""
    }, {
      "id": "98edfb56-ae61-464b-ab9c-c62972ecf72e",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.header-logo img",
      "targets": [
        ["css=.header-logo img", "css:finder"],
        ["xpath=//img[@alt='Teton Chamber of Commerce Logo']", "xpath:img"],
        ["xpath=//div[@id='content']/header/div/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "c912a5de-a40a-4ba3-92f9-433f55e9d287",
    "name": "Visit Home Page",
    "commands": []
  }, {
    "id": "b5a012e4-3d03-4cf1-9880-0f6257dd336c",
    "name": "Verify Heading",
    "commands": [{
      "id": "0095742e-de6e-43ff-967f-840c8f5e9b5f",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "72c406e1-c5d4-48df-86bc-0f2b7cda8f2f",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "68c1d382-783c-41f7-b4a4-40580535112b",
      "comment": "",
      "command": "assertText",
      "target": "css=.header-title > h1",
      "targets": [
        ["css=.header-title > h1", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h1", "xpath:idRelative"],
        ["xpath=//h1", "xpath:position"],
        ["xpath=//h1[contains(.,'Teton Idaho')]", "xpath:innerText"]
      ],
      "value": "Teton Idaho"
    }, {
      "id": "87768d6a-f49f-48f7-9d14-d94e3dabad68",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.header-title > h1",
      "targets": [
        ["css=.header-title > h1", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h1", "xpath:idRelative"],
        ["xpath=//h1", "xpath:position"],
        ["xpath=//h1[contains(.,'Teton Idaho')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "c5722666-de8a-4854-a080-b60039b5ea2b",
    "name": "Check Page Title",
    "commands": [{
      "id": "d9490fa8-32e1-4771-a3ef-a1bc73b805dd",
      "comment": "",
      "command": "assertTitle",
      "target": "Teton Idaho CoC",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "0448bc99-6861-4559-a879-1d60e3ccaa06",
    "name": "Check Spotlights",
    "commands": [{
      "id": "6ca8ca27-87a5-470c-ace7-a89a7a7705f8",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "2b0014d9-8341-4f51-ad85-8635fc25fcd0",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "51551555-93d6-405b-b050-d8ee04d4ba3f",
      "comment": "",
      "command": "click",
      "target": "css=.main-news > h3",
      "targets": [
        ["css=.main-news > h3", "css:finder"],
        ["xpath=//div[@id='content']/main/section[4]/h3", "xpath:idRelative"],
        ["xpath=//section[4]/h3", "xpath:position"],
        ["xpath=//h3[contains(.,'Race to the Moon at Teton Elementary')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "44037eb1-3572-4898-9e41-55099e77c601",
      "comment": "",
      "command": "click",
      "target": "css=.main-news > .centered-image",
      "targets": [
        ["css=.main-news > .centered-image", "css:finder"],
        ["xpath=//div[@id='content']/main/section[4]/p", "xpath:idRelative"],
        ["xpath=//section[4]/p", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f90a640a-c5d8-4fe7-be1c-676570127b6c",
      "comment": "",
      "command": "click",
      "target": "css=.spotlight1",
      "targets": [
        ["css=.spotlight1", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div", "xpath:idRelative"],
        ["xpath=//section[5]/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "32ae617b-8b8f-4c33-a870-c8ae79dd0e43",
      "comment": "",
      "command": "click",
      "target": "css=.main-news > h3",
      "targets": [
        ["css=.main-news > h3", "css:finder"],
        ["xpath=//div[@id='content']/main/section[4]/h3", "xpath:idRelative"],
        ["xpath=//section[4]/h3", "xpath:position"],
        ["xpath=//h3[contains(.,'Race to the Moon at Teton Elementary')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "51c67113-3d95-4f7c-b2c2-d214e3e44450",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.main-news > h3",
      "targets": [
        ["css=.main-news > h3", "css:finder"],
        ["xpath=//div[@id='content']/main/section[4]/h3", "xpath:idRelative"],
        ["xpath=//section[4]/h3", "xpath:position"],
        ["xpath=//h3[contains(.,'Race to the Moon at Teton Elementary')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "68ba9884-40d3-4fbe-8f01-3f755c574ab5",
      "comment": "",
      "command": "assert element count",
      "target": "css=.spotlight",
      "targets": [],
      "value": "2"
    }]
  }, {
    "id": "00c4c341-f611-4a6f-a232-d213d55dbdd8",
    "name": "Check Join Us Link",
    "commands": [{
      "id": "6fb0b670-e525-4ad1-8176-b4c8f2421cf8",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "41ebd62b-bf1e-4408-876b-bf07f152f17f",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "44c82097-0807-41ad-aa24-fee4a941155b",
      "comment": "",
      "command": "assertElementPresent",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "31d70da1-889a-4512-a6ac-50d70e3af82f",
    "name": "Check Join Us URL",
    "commands": [{
      "id": "da1773f7-e1e7-46a9-9cc6-ed484b32ef89",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "6b5abdc9-f8f9-4a37-826f-7135435e78b6",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "dbd51649-eb19-4db7-833f-0ac792d6c776",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us",
      "targets": [
        ["linkText=Join Us", "linkText"],
        ["css=.a-button:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us')]", "xpath:link"],
        ["xpath=//section[@id='nopad']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[2]", "xpath:href"],
        ["xpath=//section/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "933eaa8c-f62e-4fdb-b75c-17a06f2dabce",
      "comment": "",
      "command": "click",
      "target": "css=body",
      "targets": [
        ["css=body", "css:finder"],
        ["xpath=//body", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ce81bb94-dec8-480e-b71a-837651105801",
      "comment": "",
      "command": "assert url",
      "target": "",
      "targets": [],
      "value": "*/join.html"
    }]
  }, {
    "id": "1ae8aaa4-b9fa-49dd-be2e-0ea46eacf8cc",
    "name": "Directory Grid View",
    "commands": [{
      "id": "5027736a-2bd9-4995-b0cc-65424ee209bf",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "6ddc52b1-1c2c-4bf6-8553-d805d0ef18e2",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "7d26444d-0722-499c-a42a-7dbc270e0a4c",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d2807021-dcd1-48ea-85ac-1154e7c81d63",
      "comment": "",
      "command": "click",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d902599a-5053-4d8e-b3f9-85a6f15c4fd9",
      "comment": "",
      "command": "assertElementPresent",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "49607948-5461-405f-84ff-8afa7218141b",
    "name": "Directory List View",
    "commands": [{
      "id": "eff0baf2-0e6f-461e-9322-59679ae4c0da",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "ac1e812b-a123-4a45-9b2a-c4c2405849ed",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "8846f211-b004-4323-84eb-5656f4af75e5",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f45af296-6362-402a-9800-ef751ac83e8f",
      "comment": "",
      "command": "mouseDownAt",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": "20.83331298828125,26"
    }, {
      "id": "e3ac3d7b-53c1-491d-ae2a-95feea50e1df",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": "20.83331298828125,26"
    }, {
      "id": "0a8a32fd-e6e5-4331-83d1-0dc1e3ec10f5",
      "comment": "",
      "command": "mouseUpAt",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": "20.83331298828125,26"
    }, {
      "id": "745b439c-37db-4f46-aa06-abfe2ff5056e",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "8056ca79-03bb-4443-b9e1-f7d636fc7d1b",
      "comment": "",
      "command": "assertElementPresent",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "fb976fff-e380-4927-8cf1-582bc563f85c",
    "name": "Join Page Form",
    "commands": [{
      "id": "99ca2424-7f4d-40d8-909f-4d90c158ca6a",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "7f8121a7-2f86-4a8c-aecf-4a0d3b923942",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "620ab766-4988-4cad-93a4-687408114510",
      "comment": "",
      "command": "click",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "13b94fed-9e0c-433f-a8f9-4901bdd80af3",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a6f60e99-6d1b-4b57-82b2-f73d532b7c4a",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "olueaniyi"
    }, {
      "id": "40a1b45e-8e0d-4453-b2bc-2e63f6bfdc74",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0dd2c2e6-af0f-44aa-8eab-eb9a1ae18dfd",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "akin"
    }, {
      "id": "645dc35b-23e3-471c-bc54-cf4d05d2d7d8",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eba2af30-7ee9-484e-8248-ec2727775c40",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0f1083b4-916e-4d2e-8d40-a9745848ee9f",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1d115455-a8c5-46b0-9498-912df9a61038",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "bb"
    }, {
      "id": "74e4657c-a687-485e-aa0b-6379c83cd823",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "46dce458-6916-4a28-9cd8-1351af97b378",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "bbb"
    }, {
      "id": "62bd57a5-a370-46d4-ab2c-59bc98b937e9",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1ee5d9c2-9eee-402e-bcc3-6e02d939800f",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ff877665-1838-4df6-a6e5-665fba04b0e7",
      "comment": "",
      "command": "type",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "yyhhh@gmail.com"
    }, {
      "id": "cf015620-34c5-4328-b646-da9407b4dee1",
      "comment": "",
      "command": "click",
      "target": "name=cellphone",
      "targets": [
        ["name=cellphone", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='cellphone']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f503dc29-ecdd-4998-ac42-1b971f016719",
      "comment": "",
      "command": "type",
      "target": "name=cellphone",
      "targets": [
        ["name=cellphone", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='cellphone']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "1234567884"
    }, {
      "id": "c56afb36-2b5d-4137-b8bd-820a5d3c9bdb",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=fieldset > input", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ab5c7dcc-44cd-4180-b138-42d63eff239e",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=fieldset > input", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "aba8815c-9881-4e52-8f45-02b060b1f04e",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(16)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d49b31bc-5e0f-4268-82be-9ab08243a190",
      "comment": "",
      "command": "click",
      "target": "css=.myradio:nth-child(12)",
      "targets": [
        ["css=.myradio:nth-child(12)", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label", "xpath:idRelative"],
        ["xpath=//label", "xpath:position"],
        ["xpath=//label[contains(.,'Non-Profit')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "1989608e-30d0-48a5-9dc7-fe2ea5e9f3ae",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(16)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "573cbe48-b843-4345-9602-e79fcd744133",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=fieldset > input", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "5ce9ad8e-bf64-4428-a310-1aec4858dd20",
    "name": "Admin Page Login Error",
    "commands": [{
      "id": "3f39881c-080c-43d2-b769-6557bca580b4",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5500/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "db375876-9bbe-422e-be76-f1a5ca933005",
      "comment": "",
      "command": "setWindowSize",
      "target": "1382x744",
      "targets": [],
      "value": ""
    }, {
      "id": "9ec13638-b401-4ce1-a5d3-52577a8944dc",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "64d0a8ec-d4c3-4661-9b2a-6b8958e606c8",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "45f8aa27-5abd-48ef-aa1b-fdb7e1ba4621",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "sdsdwe"
    }, {
      "id": "af9805c2-14c4-4fcd-b7f1-d5b5858fb4cb",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6d1d6317-18d2-46e7-ac7e-af71639210eb",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "wwwww"
    }, {
      "id": "ed381891-c3fe-4b16-b1b2-c085e8f2e602",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "08671502-0bd7-4880-ac6c-8ef39702232c",
      "comment": "",
      "command": "assertValue",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": "Login"
    }, {
      "id": "b3ce60fe-c239-48c7-a72e-0e33d50ebda1",
      "comment": "",
      "command": "error message appears",
      "target": "",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "c653c260-fffd-436e-ab3e-37ffbc731229",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["c7ee5ded-a2f6-4c8e-b846-4676d8a1667d"]
  }],
  "urls": [],
  "plugins": []
}