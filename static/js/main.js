new ClipboardJS('.clipboard');
let bitcoinCp = new ClipboardJS('#bitcoinAddress', {
    text: function () {
        return 'bc1qw2wcu29rc75hqejsshmq0x4s697wntyanurwu9'
    }
});
let ethereumCp = new ClipboardJS('#ethereumAddress', {
    text: function () {
        return '0x04d238875e55bc5c8a6cc520fb6859fea876a94f'
    }
});
const $secretKey = $('#secretKey');
const $generateBtn = $('#generate');
const $copyBitcoin = $('#bitcoinAddress');
const $copyEthereum = $('#ethereumAddress');
const theme = localStorage.getItem('theme');
const possible = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)';
let popupStack = {
    position: 'left center',
    target: '.icon.input',
    on: 'click',
    title: 'Click on Generate!',
    content: '',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
    exclusive: !0,
};

$secretKey.popup(popupStack);
$generateBtn.popup({
    position: 'left center',
    target: '.icon.input',
    on: 'click',
    title: 'Copied!',
    content: 'Just paste it to settings.',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
    exclusive: !0,
});
$generateBtn.click(function () {
    getNew();
});

bitcoinCp.on('success', function (e) {
    $copyBitcoin.html('Copied!');
    $copyBitcoin.addClass('positive');

    setTimeout(function () {
        $copyBitcoin.html('Copy');
        $copyBitcoin.removeClass('positive')
    }, 1500);
    e.clearSelection()
});
ethereumCp.on('success', function (e) {
    $copyEthereum.html('Copied!');
    $copyEthereum.addClass('positive');

    setTimeout(function () {
        $copyEthereum.html('Copy');
        $copyEthereum.removeClass('positive')
    }, 1500);
    e.clearSelection()
});

$('h1.ui.header').transition('pulse');
if (theme && theme === 'dark')  {
    $('.light').toggleClass('dark').removeClass('light');
    $('#github-logo').attr('src', 'static/images/gh-mark-light.svg');
    $('div#dark-mode').addClass('checked');
    $('div#dark-mode input').attr('checked', 'checked');
};
$('#dark-mode').checkbox({
    onChecked: function () {
        $('.light').toggleClass('dark').removeClass('light');
        $('#github-logo').attr('src', 'static/images/gh-mark-light.svg');
        localStorage.setItem('theme', 'dark');
    },
    onUnchecked: function () {
        $('.dark').toggleClass('light').removeClass('dark');
        $('#github-logo').attr('src', 'static/images/gh-mark-dark.svg');
        localStorage.setItem('theme', 'light');
    }
});
$('#policy').click(function () {
    $('#policyModal').modal('show').modal({
        transition: 'pulse',
        closable: !0,
    })
});
$('#why').click(function () {
    $('#whyModal').modal('show').modal({
        transition: 'pulse',
        closable: !0,
    })
});
$('#help').click(function () {
    $('#helpModal').modal('show').modal({
        transition: 'pulse',
        closable: !0
    })
});
$('#donate').popup({
    target: '#donate',
    on: 'click',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
});

function generateKey() {
    let newSecretKey = '';

    for (let i = 0; i < 50; i++) {
        newSecretKey += possible.charAt(Math.floor(Math.random() * possible.length));
    }

    return newSecretKey;
}

function getNew() {
    $generateBtn.addClass('loading');

    let newSecretKey = generateKey();

    popupStack.title = 'Copied!';
    popupStack.content = 'Just paste it to settings.';

    $secretKey.val(newSecretKey);
    $secretKey.popup(popupStack);

    new ClipboardJS('.clipboard', {
        text: function () {
            return newSecretKey
        }
    });

    setTimeout(function () {
        $generateBtn.removeClass('loading')
    }, 200)
}
